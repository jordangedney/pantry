jQuery('document').ready(function(){
	jQuery('.content').on('click', '.panel h2', function(){
		expand(jQuery(this).parent('.panel'));
	});
	$('#search-button').click(function() {
		var input = $('#search-bar').val();
		if(input.length == 0) {
			console.log(input);
			return false;
		}
	});
	//SlimScroll plug-in for recipe instructions
	$(function(){
	    $('.inner-div').slimScroll({
	        height: '200px',
	        wheelStep: '2'
	    });
	});
});
function expand(panel){
	panel.switchClass('','expanded', 500);
	var recipeName = panel.children('h2').fadeOut(500).text();
	var collapseButton = panel.find('span.close a');
	collapseButton.click(function(){
		collapse(panel);
	});
	
}
function collapse(panel){
	panel.find('.recipe-content').remove();
	panel.find('h2').fadeIn(500);
	panel.switchClass('expanded', '', 500);
}
