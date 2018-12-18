var token = '{{csrf_token}}';

$('#Phones>li>a').on('click', function() {
    number = $('#Phones>li>a').html();
      $.ajax( {
        headers: { "X-CSRFToken": token },
        beforeSend: function() {
        $('#data').empty();
        $('#data').append('\
        <div id="circle">\
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
        $('#circle').hide('slow');
      },
      method: 'POST',
      url: ("record/number/" + number + "/"),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function( data ) {
        $('#circle').hide('slow');
        for(var i in data) {
          str = "<li class=\"btn btn-block btn-primary\" filename=\""
          + data[i]['filename'] +"\">"+data[i]['data'] + " " + data[i]['extern'] +"</li>";
          li = $('#data').append(str);
          li.children().last().wrap("<p class=record></p>");
        }
        console.log(data)
      }
    }).done(function() {
      $('.record li').on('click', function(event){
        filename = this.attributes.filename.value;
        parent = $(this.parentElement)
        console.log(parent)
        $.ajax ( {
          headers: { "X-CSRFToken": token },
          beforeSend : function() {
            $('.player').hide('slow');
            $('.player').remove();
          },
          method: 'POST',
          url: ("convert" + filename),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function( data ) {
            console.log(parent.parent);
            parent.append("<audio class='player' src=http://lk.ath.ru/ogg/"+filename.substr(1, filename.length - 4) +
            "ogg controls>play record</audio>");
          }
        }).done(function(){
          $('.player').show('slow')
        });
      });
    });
});
