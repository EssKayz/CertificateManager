function checkPasswordMatch() {
	var password = $("#password").val();
	var confirmPassword = $("#password_confirmation").val();

	if (password != confirmPassword) {
		$("#divCheckPasswordMatch").html("Passwords do not match!");
		$("#registerBtn").prop("disabled", true);
	}
	else {
		$("#divCheckPasswordMatch").html("");
		$("#registerBtn").prop("disabled", false);
	}
}