var token = '{{csrf_token}}';


Date.prototype.addHours = function(h) {
   this.setTime(this.getTime() + (h*60*60*1000));
   return this;
}

Date.prototype.StartDate = function () {
  return new Date(this.getFullYear(), this.getMonth(), this.getDate());
};

Date.prototype.EndDate = function () {
  return new Date(this.getFullYear(), this.getMonth(), this.getDate(), 23, 59);
};

$('.dataBefore').val(new Date().StartDate().addHours(3).toJSON().slice(0,19));
$('.dataAfter').val(new Date().EndDate().addHours(3).toJSON().slice(0,19));
$('.container').css('margin-left','1%')

$('#number_phone').typeahead({
  source: [],
  items: 10,
  scrollBar: false,
  alignWidth: true,
  menu: '<ul class="typeahead dropdown-menu"></ul>',
  item: '<li><a href="#"></a></li>',
  displayField: 'name',
  valueField: 'id',
  ajax: {
    url: ('autocomplete/'),
    triggerLength: 3,
  }
});

$('button').on('click', function(){
  phoneNum = $('#number_phone').val();
  before = $('.dataBefore').val();
  after = $('.dataAfter').val();
  $.ajax({
      headers: { "X-CSRFToken": token },
      beforeSend: function() {
      $('#in').empty();
      $('#out').empty();
      $('.table').empty();
      $('.table').append('\
      <div class="circle">\
      <div class="loader">\
      <div class="loader">\
      <div class="loader">\
         <div class="loader">\
\
         </div>\
      </div>\
  </div>\
</div>\
</div> ');
    },
    compile : function() {
      $('.circle').hide('slow');
      $('.circle').remove();
    },
    method: 'POST',
    url: ("number/" + phoneNum),
    data: JSON.stringify( {
      "Before": before,
      "After": after,
      "phoneNum": phoneNum
      } ),
      contentType: "application/json; charset=utf-8",
      //processData: false,
      dataType: "html",
      success: function( data ) {
        console.log(data);
        $('.table').html(data)
      }
  });
  return false;
});
