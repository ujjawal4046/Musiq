// $('.dropdown-toggle').dropdown();


$('.dropdown-toggle').click(function() {
	el = $(this).parent().find('.dropdown-menu');
	flag = el.hasClass('show');
	if (flag) {
		el.hide();
		el.addClass('hide').removeClass('show');
	} else {
		el.show();
		el.addClass('show').removeClass('hide');

	}
})
