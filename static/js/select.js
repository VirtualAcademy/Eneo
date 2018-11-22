// WIP

/* To Do:
1. Selecting a new plan from the drop down menu will regenerate the data associated below.
2. On-click for description title to show specific description below; one description opens all.
3. Prices recalculate as you select different features.
*/

$('.heading').each(function(){
  var $content = $(this).closest('thead').find('ul');
  $(this).click(function(e){
    e.preventDefault();
    $content.not(':animated').slideToggle();
  });
});

$('.feat td:first-child').each(function(){
  var $content = $(this).closest('table').find('.desc');
  $(this).click(function(e){
    e.preventDefault();
    $content.not(':animated').slideToggle();
  });
});

$("input[type='checkbox']").click(function() {
  if($(this).prop('checked'))
    $(this).closest('td').addClass('color');
  else
    $(this).closest('td').removeClass('color');
});
