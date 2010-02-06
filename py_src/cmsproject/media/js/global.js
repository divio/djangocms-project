function nospam(){	
	var p = $.makeArray(arguments).reverse().join(".").split('#'); m = p[1] + "@" + p[0];
	document.write('<a href="mailto:'+m+'?subject=Kontakt">'+m+'</a>');		
}

/* Communicate swf/js */
function swfPath(swfid) {
    if(navigator.appName.indexOf("Microsoft") != -1){
		return window[swfid]
    }else{
		return document[swfid]
    }
}

$(function(){
	$.easing.easeOutQuart = function (x, t, b, c, d) {
	    return -c * ((t=t/d-1)*t*t*t - 1) + b;
	};

	$.fn.duplicate = function(count, cEvents) {
		var tmp = [];
		for (var i=0; i<count; i++){
			$.merge(tmp, this.clone(cEvents).get());
		}
		return this.pushStack(tmp);
	};
	
	$(".togglepageheader").click(function() {
		togglepageheader();
		return false;
	})	
	
	function togglepageheader(){
		$("#pageheader").slideToggle(500);
		 $(".togglepageheader").toggleClass("open");
	}
	
	/* Searchbox */
	$("#searchbox input[type=text]").fieldtag();
	
	//$("ul.dropdown li ul li:has(ul)").find("a:first").append(" &raquo; ");
});
