/*
 * jQuery Styled Select Boxes
 * version: 1.1 (2009/03/24)
 * @requires jQuery v1.2.6 or later
 *
 * Examples and documentation at: http://code.google.com/p/lnet/wiki/jQueryStyledSelectOverview
 *
 * Copyright (c) 2008 Lasar Liepins, liepins.org, liepins@gmail.com
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * edit by FJ (2009/08/12)
 * new clickOption function that gives you a change event $('select').change(function(){ });
 * new selectMinWidth, selectMaxWidth, selectAdditionalWidth options $('select').styledSelect({selectMinWidth:120,selectMaxWidth:500});
 */

jQuery.fn.styledSelect=function(settings){
	settings = jQuery.extend({
		selectClass: 'styledSelect',
		selectMinWidth: 100,
		selectMaxWidth: 960,
		selectAdditionalWidth: 40,
		openSelectClass: 'open',
		optionClass: 'option',
		selectedOptionClass: 'selected',
		closedOptionClass: 'closed',
		firstOptionClass: 'first',
		lastOptionClass: 'last',
		zIndexApply: false,
		zIndexStart: 250,
		deactiveOnBackgroundClick: true
	}, settings);	

	var currentZIndex = settings.zIndexStart;

	this.each(function(){
		var s = jQuery(this);
		var cs = jQuery('<div></div>').attr('class', settings.selectClass);
		if(settings.zIndexApply){ cs.css('z-index', currentZIndex-2); };
		var csl = jQuery('<ul></li>');
		if(settings.zIndexApply){ csl.css('z-index', currentZIndex-1); };
		cs.append(csl);
		s.hide(0).after(cs);
		cs = s.next();	

		jQuery('option', s).each(function(){if(jQuery(this).attr('value')==undefined){jQuery(this).attr('value', jQuery(this).text());}});

		var closedSelect=function(){
			jQuery('ul', cs).html('');
			addOption(s.val(), jQuery(':selected', s).text(), clickSelect);
			cs.removeClass(settings.openSelectClass);
			jQuery('ul li', cs).removeClass(settings.selectedOptionClass).removeClass(settings.optionClass).addClass(settings.closedOptionClass);
			if(settings.deactiveOnBackgroundClick){$(document).unbind('mousedown', closedSelect);cs.unbind('mousedown');}
		};

		var clickSelect=function(){
			jQuery('ul', cs).empty();
			jQuery('option', s).each(function(i){addOption(jQuery(this).val(), jQuery(this).text(), clickOption); });
			cs.addClass(settings.openSelectClass);
			jQuery('ul li:first-child', cs).addClass(settings.firstOptionClass);
			jQuery('ul li:last-child', cs).addClass(settings.lastOptionClass);
			if(settings.deactiveOnBackgroundClick){$(document).bind('mousedown', closedSelect);cs.bind('mousedown', function(){return false;});}
		};

		var clickOption=function(){var val=jQuery(this).attr('rel');s.val(val);s.change();};

		var addOption=function(optVal, optName, callBack){
			var cso = jQuery('<li></li>').attr('rel', optVal).text(optName).click(callBack).addClass(settings.optionClass);
			if(settings.zIndexApply){cso.css('z-index', currentZIndex);};
			if(s.val()==optVal){cso.addClass(settings.selectedOptionClass);};
			jQuery('ul', cs).append(cso);
		};

		closedSelect();
		s.change(closedSelect);
		currentZIndex -= 3;
				
		var w = Math.max(settings.selectMinWidth,jQuery('ul', cs).find("li").width()+settings.selectAdditionalWidth);
		if(w>settings.selectMaxWidth){w=settings.selectMaxWidth;}				
		jQuery('ul', cs).width(w);
	});
	
	return this;
};
