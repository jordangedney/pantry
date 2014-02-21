jQuery('document').ready(function(){
	jQuery('.result').on('click', '.panel h2', function(){
		jQuery(this).parent('.panel').addClass('expanded');
	});
});
