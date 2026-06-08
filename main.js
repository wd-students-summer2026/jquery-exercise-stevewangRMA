// this is your custom Javascript file

$(function () {
  // add any custom Javascript code below this line

  $('.cocktail-name').on('mouseover', function () {
    var story = $(this).data('desc');
    $('#cocktail-desc').text(story);
  });
  $('.cocktail-name').on('mouseout', function () {
    $('#cocktail-desc').text('Hover over any drink name above to read its story.');
  });

  var $img = $('#swap-img');
  var originalSrc = $img.attr('src');
  var hoverSrc = $img.data('hover');
  $img.on('mouseover', function () {
    $(this).attr('src', hoverSrc);
  });
  $img.on('mouseout', function () {
    $(this).attr('src', originalSrc);
  });

  $('#shake-btn').on('click', function () {
    $('#garnish')
      .animate({ left: '+=260px' }, 600)
      .animate({ top:  '-=20px'  }, 250)
      .animate({ left: '0px', top: '24px' }, 700);
  });
  // add any custom Javascript code above this line.
})
