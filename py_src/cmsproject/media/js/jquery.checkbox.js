/**
 * jQuery custom checkboxes
 * 
 * Copyright (c) 2008 Khavilo Dmitry (http://widowmaker.kiev.ua/checkbox/)
 * Licensed under the MIT License:
 * http://www.opensource.org/licenses/mit-license.php
 *
 * @version 1.3.0 Beta 1
 * @author Khavilo Dmitry
 * @mailto wm.morgun@gmail.com
 * updated by FJ: add change listener
**/

(function($){
var CB = function(e){
	if(!e) var e = window.event;
	e.cancelBubble = true;
	if(e.stopPropagation) e.stopPropagation();
};
	
$.fn.checkbox = function(options) {
try	{document.execCommand('BackgroundImageCache', false, true);} catch(e){}
var settings = {cls:'jquery-checkbox',empty:'/media/img/empty.png'};
settings = $.extend(settings, options || {});

var addEvents = function(object){
	var checked = object.checked;
	var disabled = object.disabled;
	var $object = $(object);
	
	if(object.stateInterval) clearInterval(object.stateInterval);
	
	object.stateInterval = setInterval(
		function(){
			if(object.disabled != disabled) $object.trigger((disabled = !!object.disabled) ? 'disable' : 'enable');
			if(object.checked != checked) $object.trigger((checked = !!object.checked) ? 'check' : 'uncheck');
		}, 10
	);
	return $object;
};
	
return this.each(function(){
	var ch = this; 
	var $ch = addEvents(ch);
	if(ch.wrapper) ch.wrapper.remove();
	
	ch.wrapper = $('<span class="' + settings.cls + '"><span class="mark"><img src="' + settings.empty + '" /></span></span>');
	ch.wrapperInner = ch.wrapper.children('span:eq(0)');
	ch.wrapper.hover(
		function(e){ch.wrapperInner.addClass(settings.cls + '-hover');CB(e);},
		function(e){ch.wrapperInner.removeClass(settings.cls + '-hover');CB(e);}
	);
	
	$ch.css({position: 'absolute', zIndex: -1, visibility: 'hidden'}).after(ch.wrapper);
	
	var label = false;
	if($ch.attr('id')){
		label = $('label[for='+$ch.attr('id')+']');
		if(!label.length) label = false;
	}
	if(!label){
		label = $ch.closest ? $ch.closest('label') : $ch.parents('label:eq(0)');
		if(!label.length) label = false;
	}
	if(label){
		label.hover(function(e){ch.wrapper.trigger('mouseover',[e]);},function(e){ch.wrapper.trigger('mouseout',[e]);});
		label.click(function(e){$ch.trigger('click',[e]);CB(e);$ch.change();return false;});
	}
	ch.wrapper.click(function(e){$ch.trigger('click',[e]);CB(e);$ch.change();return false;});
	$ch.click(function(e){CB(e);});
	$ch.bind('disable',function(){ch.wrapperInner.addClass(settings.cls+'-disabled');}).bind('enable',function(){ch.wrapperInner.removeClass(settings.cls+'-disabled');});
	$ch.bind('check',function(){ch.wrapper.addClass(settings.cls+'-checked');}).bind('uncheck',function(){ch.wrapper.removeClass(settings.cls+'-checked');});
	
	$('img', ch.wrapper).bind('dragstart',function(){return false;}).bind('mousedown',function(){return false;});
	
	if(window.getSelection)	ch.wrapper.css('MozUserSelect', 'none');
	
	if(ch.checked) ch.wrapper.addClass(settings.cls + '-checked');
	if(ch.disabled) ch.wrapperInner.addClass(settings.cls + '-disabled');			
});
}
})(jQuery);
