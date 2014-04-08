jQuery('document').ready(function(){
	jQuery('.result').on('click', '.panel h2', function(){
		expand(jQuery(this).parent('.panel'));
	});
	$('#search-button').click(function() {
		var input = $('#search-bar').val();
		if(input.length == 0) {
			console.log(input);
			return false;
		}
		console.log(input);
	});
});
function expand(panel){
	panel.switchClass('','expanded', 500);
	var recipeName = panel.find('h2').fadeOut(500).text();
	var contentDiv = jQuery('<div></div>',{
		"class":"recipe-content"
	});
	
	var header = jQuery('<h1>'+recipeName+'</h1>');
	var collapseButton = jQuery('<span class="close">collapse</span>');
	collapseButton.click(function(){
		collapse(panel);
	});
	header.append(collapseButton);
	contentDiv.append(header);
	$('.recipe-left').show();
	//var ingredientsDiv = jQuery('<div class="recipe-left recipe-info"><h2>Ingredients</h2></div>');
	contentDiv.append(ingredientsDiv);
	$('.recipe-center').show();
	//var ingredientsDiv = jQuery('<div class="recipe-center recipe-info"><h2>Details</h2></div>');
	$('.recipe-center').show();
	contentDiv.append(ingredientsDiv);
	
	//var ingredientsDiv = jQuery('<div class="recipe-right recipe-info"><h2>Other</h2></div>');
	contentDiv.append(ingredientsDiv);
	panel.append(contentDiv);
}
function collapse(panel){
	panel.find('.recipe-content').remove();
	panel.find('h2').fadeIn(500);
	panel.switchClass('expanded', '', 500);
}
