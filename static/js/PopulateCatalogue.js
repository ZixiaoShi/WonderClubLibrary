/**
 * Created by freeze on 2015-11-01.
 */
function NewThumbNail(book){
  $(".thumbnails").append($('<li>')
          .addClass('span2')
          .append($('<div>')
                  .addClass("thumbnail")
                  .append($('<img>')
                          .attr('id',book.isbn))
                  .append($('<div>')
                          .addClass("caption")
                          .append($('<h4>')
                                  .text(book.title))
                          .append($('<h5>')
                                  .text(book.author))
                          .append($('<h5>')
                                  .text(AvailableText(book)))
                          .append($('<button>')
                                  .addClass('btn')
                                  .addClass('reserve')
                                  .text("Reserve")
                                  .attr("value", book.id)
                                  .prop('disabled', !CheckAvailability(book)))

          )

  ))
}

function CheckAvailability(book){
    if ( book.renter == null || book.local_avail == "false"){
        return true;
    }
    else{
        return false;
    }
}

function AvailableText(book){
    if (CheckAvailability(book)){
        return "Available";
    }
    else{
        return "Borrowed Until " + book.duedate;
    }
}

function ImgURL(element){
    DOUBAN.apikey = '05a5b9a293fb48d010f12ce7bbf1da70';
    DOUBAN.getISBNBook({
        'isbn':element.attr('id'),
        callback:function(re){
            var book = DOUBAN.parseSubject(re);
            if (book.link.image){
                console.log(book.link.image);
                element.attr('src', book.link.image);
            }
        }
    });
}

$(document).ready(function(){
    $(".thumbnails").on("click",".btn.reserve",function(){
        //alert("reserve book");
        var reserve_url = "reserve/" + $(this).val() + "/";
        //console.log(reserve_url);
        //window.open(url);
        checkAuth();
        $("#myModal").modal();
        $.ajax({url:reserve_url,success:function(data) {
            console.log(data);
            //alert(data);
        }});
    });
});
