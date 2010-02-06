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