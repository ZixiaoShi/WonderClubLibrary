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
                                  .text(CheckAvailability(book)))
                          .append($('<a>')
                                  .addClass('btn')
                                  .addClass('reserve')
                                  .text("Reserve"))
          )

  ))
}

function CheckAvailability(book){
    if ( book.renter == null){
        return "Available"
    }
    else{
        return "Borrowed Until " + book.duedate
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