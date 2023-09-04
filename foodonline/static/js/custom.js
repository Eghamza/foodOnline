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
          swal.fire("login", response.message, "info").then(function(){
            window.location = '/login';
          })
        } else if (response.status == "failed") {
          swal(response.message, "", "error");
        }
        else{

            $("#cart_counter").html(response.cart_counter["cart_counter"]);
            $("#qty-" + food_id).html(response.qty);
        }
      },
    });
  });

  // dicrease the cart items
  $(".dicrease_cart").on("click", function (e) {
    e.preventDefault();

    food_id = $(this).attr("data-id");
    url = $(this).attr("data-url");

    $.ajax({
      type: "GET",
      url: url,

      success: function (response) {
        if (response.status == "success") {
       
            $("#cart_counter").html(response.cart_counter["cart_counter"]);
            $("#qty-" + food_id).html(response.qty);
        }
        else if (response.status == "login_requered") {
            swal.fire("login", response.message, "info").then(function(){
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

  // place item quentity

  $(".qty_item").each(function () {
    var the_id = $(this).attr("id");

    var qty = $(this).attr("data-qty");

    $("#" + the_id).html(qty);
  });
});
