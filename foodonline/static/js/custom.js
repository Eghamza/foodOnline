$(document).ready(function () {
  //add to cart
  $(".add_to_cart").on("click", function (e) {
    e.preventDefault();

    food_id = $(this).attr("data-id");
    url = $(this).attr("data-url");
    data = { food_id: food_id };
    $.ajax({
      type: "GET",
      url: url,
      data: data,
      success: function (response) {
        if (response.status == "login_requered") {
          swal.fire("login", response.message, "info").then(function () {
            window.location = '/login';
          })
        } else if (response.status == "failed") {
          swal(response.message, "", "error");
        }
        else {

          $("#cart_counter").html(response.cart_counter["cart_counter"]);
          $("#qty-" + food_id).html(response.qty);
          $("#subtotal").html(response.amount["subtotal"]);
          $("#tex").html(response.amount["tex"]);
          $("#total").html(response.amount["grandtotal"]);
        }
      },
    });
  });

  // dicrease the cart items
  $(".dicrease_cart").on("click", function (e) {
    e.preventDefault();

    food_id = $(this).attr("data-id");
    cart_id = $(this).attr("id");
    url = $(this).attr("data-url");

    $.ajax({
      type: "GET",
      url: url,

      success: function (response) {
        if (response.status == "success") {

          $("#cart_counter").html(response.cart_counter["cart_counter"]);
          $("#qty-" + food_id).html(response.qty);
          $("#subtotal").html(response.amount["subtotal"]);
          $("#tex").html(response.amount["tex"]);
          $("#total").html(response.amount["grandtotal"]);




          //hubi in uu url ku joogo /cart/
          if (window.location.pathname == '/cart/') {
            removecart(response.qty, cart_id)
            display_empty_message()

          }


        }
        else if (response.status == "login_requered") {
          swal.fire("login", response.message, "info").then(function () {
            window.location = '/login';
          })
        }
        else if (response.status == "failed") {
          swal.fire(response.message, "", "error");
        }
        else {
          $("#cart_counter").html(response);
          $("#qty-" + food_id).html(response);
        }
      },
    });
  });


  // delete cart
  $(".delete_cart").on("click", function (e) {
    e.preventDefault();
    var id = $(this).attr("data-id");
    var url = $(this).attr("data-url");

    $.ajax({
      type: "GET",
      url: url,
      success: function (response) {

        if (response.status == "success") {
          swal.fire(response.message, '', "success").then(function () {
            removecart(0, id);
            display_empty_message()

            $("#subtotal").html(response.amount["subtotal"]);
            $("#tex").html(response.amount["tex"]);
            $("#total").html(response.amount["grandtotal"]);
          });
          $("#cart_counter").html(response.cart_counter["cart_counter"]);

        }
        else if (response.status == "Failed") {
          swal.fire(response.message, '', "error");
        }

      }
    })
  })
  // place item quentity

  $(".qty_item").each(function () {
    var the_id = $(this).attr("id");

    var qty = $(this).attr("data-qty");

    $("#" + the_id).html(qty);
  });
});
  // add opening hour
  document.getElementById('add-hour').addEventListener('click', function (e) {
    e.preventDefault();
    var day = document.getElementById('id_day').value
    var from_hour = document.getElementById('id_from_hour').value
    var to_hour = document.getElementById('id_to_hour').value
    var check = document.getElementById('id_is_closed').checked
    var url = document.getElementById('add_hour_url').value
    var csrf_token = $('input[name="csrfmiddlewaretoken"]').val()


    if (check) {
      check = 'True';
      condition = "day != ''";
    }
    else {
      check = 'False';
      condition = "day != '' && from_hour != '' && to_hour != ''";
    }
    if (eval(condition)) {
      $.ajax({
        type: 'POST',
        url: url,
        data:{
          'day': day,
          'from_hour': from_hour,
          'to_hour': to_hour,
          'csrfmiddlewaretoken': csrf_token,
          'check': check,

        },
        success: function (response) {
            if (response.status == "success"){
              if (response.is_closed == "Closed")
              {
                html = '<tr><td><b>'+response.day+'</b> </td><td> Closed </td><td> <a href="#s">Remove</a></td></tr>';
              $(".opening_hours").append(html);
              
              }
              else{

                html = '<tr><td><b>'+response.day+'</b> </td><td>'+ response.from_hour +' - '+ response.to_hour +'</td><td> <a href="#s">Remove</a></td></tr>';
                $(".opening_hours").append(html);
                
              }
              document.getElementById('opening-hours').reset()
             

            }
            else if (response.status == "Failed"){
              swal.fire(response.message,'', "error")
             

            }

        }


      })


    }
    else {
      swal.fire('please fill all fields ', '', 'info');

    };
  });
  //end documentment


//remove opening hours
$(".remove").on('click',function(e) {
  e.preventDefault();
  url = $(this).attr('data-url');
  $.ajax({
    type: "GET",
    url: url,
    success: function(response){
      if (response.status == "success")
      {
        console.log(response.message)
      }
    }
  })
})


function removecart(cart_qty, cart_id) {

  if (cart_qty <= 0) {
    document.getElementById("cart_item-" + cart_id).remove();
  }

}

// check if the cart is empty then display Empty message
function display_empty_message() {

  var cart_counter = document.getElementById("cart_counter").innerHTML;
  console.log(cart_counter);
  if (cart_counter <= 0) {
    document.getElementById("empty_cart").style.display = "block";

  }

}

