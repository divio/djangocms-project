// detects IEs
// WHY: because everybody loves IE, don't you? well, me neither
$.browser.msieLTE7 = ($.browser.msie && parseInt($.browser.version)<7); //IE<7
$.browser.msieLTE8 = ($.browser.msie && parseInt($.browser.version)<8); //IE<8
$.browser.msie8 = ($.browser.msie && parseInt($.browser.version) == 8); //IE8

// Reverse a jquery collection (last first)
// USAGE: $("div").reverse().each(function(){ //reverse order each() });
$.fn.reverse = [].reverse;

// Allows chainable logging
// USAGE: $('#someDiv').log('#someDiv').addClass('someClass');
$.fn.log = function(message){ return console && console.log("%s: %o", message, this)? this : this; };

// Check if at least one selected element exists 
// USAGE: if($.exists("div.special")){ //yes it does }
$.exists = function(selector){ return $(selector).length? true : false; }

// Computes the maximal height of an array of elements
// USAGE: var max = $("#someList li").maxHeight();
$.fn.maxHeight = function(){
	var max = 0;
	$(this).each(function(){
		var height = $(this).height();
		max = height>max? height : max;
	});
	return max;
}

//Sets an equal height of a floating collection of elements per line
//DEPENDS: maxHeight
//USAGE: $("#someList li").syncHeightPerLine();
//ALT USAGE: $.syncHeightPerLine(list);
$.fn.syncHeightPerLine = function(options){
    var conf = $.extend({
        syncDescendant: false, // change this to a child-selector for the .find() method 
        resetHeight: false // useful for reinitializations
    }, options);
    var syncList = $(this);
    if (!syncList.length) {
        return syncList;
    }
    var toSync = [];
    if (conf.resetHeight) {
        syncList.each(function(i, val){
            $(conf.syncDescendant ? $(this).find(conf.syncDescendant) : this).css("height", "auto");
        });
    }
    syncList.each(function(i, val){
        $(conf.syncDescendant ? $(this).find(conf.syncDescendant) : this).each(function(){
            toSync.push(this);
        });
        if (($(this).next().length && $(this).position().top != $(this).next().position().top) ||
        !$(this).next().length) {
            $(toSync).height($(toSync).maxHeight());
            toSync = [];
        }
    });
	return this;
};

//Adds a class name on hovering, removes it otherwise
//default class is "hover"
//USAGE: $("#someDiv").hoverClass("mouseover");
$.fn.hoverClass = function(hoverClass){
	return $(this).hover(function() {
		$(this).addClass(hoverClass || "hover");
	}, function(){
		$(this).removeClass(hoverClass || "hover");
	});
};

//Adds a bit to z-index of the element and to every parent
//USAGE: 
//	$("#someDiv").flyHigh() //sets #someDiv and every parent to its current z-index plus the default altitude (25)
///	$("#someDiv").flyHigh({altitude:-25}) //sets back #someDivs and every parents z-index
$.fn.flyHigh = function(options){ 
	var conf = $.extend({
    	altitude: 25
    }, options);
    if(!this.length){ return this; }
	$(this).each(function(){
		$($.merge( [this], $.makeArray($(this).parents()) )).each(function(){
			var zi = (parseInt($(this).css("z-index")) || 0) + conf.altitude;
			$(this).css("z-index", zi < 0 ? "0" : zi);
		});
	});
	return this;
};
