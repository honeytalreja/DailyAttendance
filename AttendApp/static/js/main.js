
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('#user');

    $('.validate-form').on('submit',function(){
        var check = true;
        if(validate(input) == false) {
            return false;
        }
        return true;
        // for(var i=0; i<input.length; i++) {
        //     if(validate(input[i]) == false){
        //         showValidate(input[i]);
        //         check=false;
        //     }
        // }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        // var passwd = $('#passwd');
        //
        // if($(input).val().trim().match('honey')) {
        //     if(passwd.val().trim().match('h')) {
        //
        //     } else {
        //         showValidate(passwd);
        //         return false;
        //     }
        // } else if($(input).val().trim().match('ria')) {
        //     if(passwd.val().trim().match('h')) {
        //
        //     } else {
        //         showValidate(passwd);
        //         return false;
        //     }
        //
        // } else if($(input).val().trim().match('pranav')) {
        //     if(passwd.val().trim().match('h')) {
        //
        //     } else {
        //         showValidate(passwd);
        //         return false;
        //     }
        //
        // } else if($(input).val().trim().match('shrirang')) {
        //     if(passwd.val().trim().match('h')) {
        //
        //     } else {
        //         showValidate(passwd);
        //         return false;
        //     }
        //
        // } else {
        //     showValidate(input);
        //     return false;
        // }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);