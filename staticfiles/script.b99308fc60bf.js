function check()
{
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var email = document.getElementById('email').value;
    var pass = document.getElementById('pass').value;
    var cpass = document.getElementById('cpass').value;
    var txt = document.getElementById('num').value;
    var phoneno = /^(01)(\d{9})$/;
    if(fname == "")
    {
        alert("enter the first name");
        return false;
    }
    else
    {
        if(lname == "")
        {
            alert("enter the last name");
            return false;
        }
        else
        {
            if(!email.includes("@"))
            {
                alert("enter a valid email");
                return false;
            }
            else
            {
                if(pass == "")
                {
                    alert("enter the password");
                    return false;
                }
                else
                {
                    if(pass != cpass)
                    {
                        alert("confirm the password");
                        return false;
                    }
                    else
                    {
                        if(!phoneno.test(txt))
                        {
                            alert("enter a valid mobile number");
                            return false;
                        }
                        else
                        {
                            if(document.getElementById('creator').checked || document.getElementById('donor').checked)
                            {
                                document.getElementById("form").submit();
                            }
                            else
                            {
                                alert("select type of user");
                                return false;
                            }
                        }
                    }
                }
            }
        }
    }
}   