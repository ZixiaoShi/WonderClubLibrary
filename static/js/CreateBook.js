/**
 * Created by freeze on 2015-10-31.
 */

$(document).ready(function(){
    $('.dateinput').datepicker({ format: "yyyy/mm/dd" });

       /** This Section Reads Book Information Using ISBN from Douban API V2 **/
    $("#readISBN").click(function(){


        var isbn = $("#id_isbn").val();
        var url = "http://api.douban.com/v2/book/isbn/" + isbn;
        DOUBAN.apikey = '05a5b9a293fb48d010f12ce7bbf1da70';
        DOUBAN.getISBNBook({
            'isbn':isbn,
            callback:function(re){
                var book = DOUBAN.parseSubject(re);
                console.log(book);
                readBookInfo(book);
                /**
                $("#id_isbn").val(book.isbn13);
                $("#id_title").val(book.title['$t']);
                $('#id_author').val(book.author.map(function(elem){
                    return elem.name['$t'];
                }).join(","));
                 **/

            }
        });
    });

    function readBookInfo(book){
        if(book.attribute.isbn13){$('#id_isbn').val(book.attribute.isbn13[0]);}
        if(book.attribute.title){$('#id_title').val(book.attribute.title[0]);}
        if(book.attribute.author){$('#id_author').val(book.attribute.author.join(","));}
        if(book.attribute.translator){$('#id_translator').val(book.attribute.translator.join(","));}
        if(book.attribute.publisher){$('#id_publisher').val(book.attribute.publisher[0]);}
        if(book.attribute.pubdate){$('#id_pubdate').val(book.attribute.pubdate[0]);}
        if(book.attribute.pages){$('#id_pages').val(book.attribute.pages[0]);}
    }
});
