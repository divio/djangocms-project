function initSimpleGallery(cms_placeholder, gallery_holder, sliderItemCountOriginal, p_i, cms_instancestyle ){
	var silderActiveId = 0;
	var silderLastActiveId = 0;
	var sliderItemCount = 0;
	var sliderItemStart = 0;
	var sliderWidth = 0;
	var sliderItemStartMiddle = false;
	
	var gallery_content 	= gallery_holder+" .gallery_content";
	var gallery_slider 		= gallery_holder+" .gallery_slider";
	var gallery_active 		= gallery_holder+" .gallery_active";
	var gallery_nav 		= gallery_holder+" .gallery_nav";

	var gallery_info 		= gallery_holder+" .gallery_info";
	var gallery_footer_info = gallery_holder+" .gallery_footer_info";

	var generateItems = function(c){
		$(gallery_nav+" li").duplicate(c).prependTo(gallery_nav);
		$(gallery_active+" .holder").duplicate(c).prependTo(gallery_active);

		$(gallery_active+" .holder").each(function(i){
			$(this).attr("title",i+1);
		});
	}
	
	var slideToItem = function(id){
		silderActiveId = Number(id);
		if(silderActiveId < 1){silderActiveId=sliderItemCount;}
		if(silderActiveId > sliderItemCount){silderActiveId=1;}

		var newX = ((silderActiveId-1)*100);
		var id2 = Number($(gallery_nav+" li:eq("+(silderActiveId-1)+")").attr("title"))-1;
		//alert(newX+" "+$("#simplegallery_{{ instance.id }} .gallery_nav li:eq("+(silderActiveId-1)+")").position().left)
		
		$(gallery_slider).stop().scrollTo({ top:0, left:newX+"px" }, 400, {easing: "easeOutQuart"} );
								
		$(gallery_content).cycle(id2);
		
		if(cms_placeholder == "feature_top" && cms_instancestyle == "infobottom"){
			var footerinfo = $(gallery_content+" .holder:eq("+id2+") .gallery_info").html();
			if(silderLastActiveId!=silderActiveId){
				$(gallery_footer_info).fadeOut(400, function(){
					$(this).html(footerinfo);
					if($.trim(footerinfo).length>0){
						$(this).fadeIn(400);
					}
				});
			}
		}
		silderLastActiveId = silderActiveId;
	}
	
		
	if(sliderItemCountOriginal == 3){
		$(gallery_holder).addClass("simplegallery_sliderart3");
		generateItems(10);
		sliderItemStartMiddle = true;
	}else if(sliderItemCountOriginal == 2){
		$(gallery_holder).addClass("simplegallery_sliderart2");
	}else if(sliderItemCountOriginal == 1){
		$(gallery_holder).addClass("simplegallery_art1");
	}else{
		$(gallery_holder).addClass("simplegallery_artnormal");
		generateItems(10);
		sliderItemStartMiddle = true;
	}

	$(gallery_slider+" .slideritem").each(function(i){
		sliderItemCount++
		sliderWidth += 200+$(this).width();
	});

	if(sliderItemStartMiddle == true){
		sliderItemStart = Math.round(sliderItemCount/2);
	}
	
	$(gallery_nav).width(sliderWidth);	
	$(gallery_nav+" li:first-child").addClass("first-child");	


	if(cms_placeholder == "feature_top"){
		$(gallery_info).height($(gallery_content).height());
	}else{
		$(gallery_info).width($(gallery_holder).width())
	}
	
	$(gallery_content).cycle({
		fx:    'fade',
        speed:  '900',
        timeout: 0
	});
	
	$(gallery_active).cycle({
        fx:    'fade',
        speed:  '900',
        timeout: (p_i*1000),
        pager:  gallery_nav,
        pagerAnchorBuilder: function(idx, slide) {
            return gallery_nav+' li:eq(' + (idx) + ') a';
        },
		next: gallery_holder+" .next",
		prev: gallery_holder+" .prev",
		startingSlide: sliderItemStart,
		before: function(currSlideElement, nextSlideElement, options, forwardFlag) {
			slideToItem($(nextSlideElement).attr("title"))
		}
	});	
}	