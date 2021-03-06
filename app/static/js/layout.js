$(document).ready(function(){
	$("#fileBox").hide()
	$("#messageBox").hide()
	$("#searchBox").hide()
	$("#submitButton").hide()
	$("#passphraseBox").hide()
	$('input:checkbox').prop('checked', false);
	$('input:radio').prop('checked', false);
	$("#messageformatfile").click(function(){
		$("#fileBox").show()
		$("#messageBox").hide()
		$("#submitButton").show()
		$("#message").val("")
	});
	$("#messageformattext").click(function(){
		$("#messageBox").show()
		$("#fileBox").hide()
		$("#submitButton").show()
		$("#file").val(null)
	});

	$("#formSubmit").click(function(){
		var checked = $('input:checked').length;
		if (checked<2){
	        alert("Please check at least one of Encyption or Sign");
	        return false;
	    }
	    if($("#messageBox").is(":visible") && $("textarea#message").val() == ""){
	    	alert("Please Enter the Message");
	    	return false;
	    }
	    if($("#fileBox").is(":visible") && $("input[name='file']").val() == ""){
	    	alert("Please Select the File");
	    	return false;
	    }
	    if($("#passphraseBox").is(":visible") && $("input[name='passphrase']").val() == ""){
	    	alert("Please Enter the Passphrase");
	    	return false;
	    }
	    if($("#searchBox").is(":visible") && $("input[name='username']").val() == ""){
	    	alert("Please Enter the Username");
	    	return false;
	    }
	    
	});
	$("#encrypt, #verify").click(function(){
		if($("#searchBox").is(":visible")){
			$("#searchBox").hide()
			$("input[name='username']").val("")
		}else{
			$("#searchBox").show()
		}
	});
	$("#sign, #decrypt").click(function(){
		if($("#passphraseBox").is(":visible")){
			$("#passphraseBox").hide()
			$("input[name='passphrase']").val("")
		}else{
			$("#passphraseBox").show()
		}
	});
	$("#formSubmitDec").click(function(){
		var checked = $('input:checked').length;
		if (checked<2){
	        alert("Please check at least one of Decryption or Verify");
	        return false;
	    }
	    if($("#messageBox").is(":visible") && $("textarea#message").val() == ""){
	    	alert("Please Enter the Message");
	    	return false;
	    }
	    if($("#fileBox").is(":visible") && $("input[name='file']").val() == ""){
	    	alert("Please Select the File");
	    	return false;
	    }
	    if($("#passphraseBox").is(":visible") && $("input[name='passphrase']").val() == ""){
	    	alert("Please Enter the Passphrase");
	    	return false;
	    }
	    if($("#searchBox").is(":visible") && $("input[name='username']").val() == ""){
	    	alert("Please Enter the Username");
	    	return false;
	    }
	});
	$("#formSubmitRev").click(function(){
		var checked = $("input[name='revoke_regen']:checked").val()
		if (checked==undefined){
	        alert("Please check at least one of Revocation or Regeneration");
	        return false;
	    }
	    if($("#passphraseBoxRev_regen").is(":visible") && $("input[name='passphrase']").val() == ""){
	    	alert("Please Enter the Passphrase");
	    	return false;
	    }
	    if(checked=="delete"){
	    	if (!confirm("Are you sure you want to revoke the key and user? This means the account will be destroyed from the system and the step is irreversible. Please choose regenerate if you want a new key. ")){
      			return false;
    		}
	    }else{
		 if (!confirm("Are you sure you want to regenerate the key? The step is irreversible. This will change you key pair of your account")){
      			return false;
    		}   
	    }
	});
});
