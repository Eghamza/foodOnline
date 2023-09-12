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
            if(window.location.pathname == '/cart/')
            {
              removecart(response.qty,cart_id)
              display_empty_message()

            }


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


  // delete cart
  $(".delete_cart").on("click", function(e){
    e.preventDefault();
    var id = $(this).attr("data-id");
    var url = $(this).attr("data-url");
   
    $.ajax({
      type: "GET",
      url:url,
      success: function(response){

        if(response.status == "success")
        {
          swal.fire(response.message,'', "success").then(function(){
            removecart(0,id);
            display_empty_message()
            
            $("#subtotal").html(response.amount["subtotal"]);
            $("#tex").html(response.amount["tex"]);
            $("#total").html(response.amount["grandtotal"]);
          });
          $("#cart_counter").html(response.cart_counter["cart_counter"]);
          
        }
        else if (response.status == "Failed"){
          swal.fire(response.message,'', "error");
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


  document.getElementById('add-hour').addEventListener('click', function(e) {
  e.preventDefault();
  alert('Please enter');
});
  //end documentment
});


function removecart(cart_qty,cart_id) {

  if ( cart_qty <= 0 ) {  
    document.getElementById("cart_item-"+cart_id).remove();
  }

}

// check if the cart is empty then display Empty message
function display_empty_message() {

  var cart_counter = document.getElementById("cart_counter").innerHTML;
  console.log(cart_counter);
  if (cart_counter <= 0)
  {
    document.getElementById("empty_cart").style.display = "block";

  }

}

