<!doctype html>
<html lang="en">
<head>
<!-- Required meta tags -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">


<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384- EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">


<title>Login</title>
</head>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384- MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>


<body style="background-color:#B2D3C2">
<div class="container mt-3">
<h1 style="color: black; text-align: center;">
Personal Expense Tracker <img src="bank.png" style="width:50px;height: 50px;">
</h1>
<div class="container mt-5" style="width: 600px;">
<div class="card shadow-lg bg-white rounded">
<div class="card-header" style="text-align: center;">
<h4>Login</h4>
</div>
<div class="card-body">
 
<form action="/login" method="POST">
<div class="mb-3">
<label for="email" class="form-label">Email: </label>
<input type="email" class="form-control" name="email" id="email" placeholder="abc@gmail.com">
</div>
<div class="mb-3">
<label for="password" class="form-label">Password: </label>
<input type="password" class="form-control" name="password" id="password"></input>
</div>
<button type="submit" style="background-color:#00AD83; border- color:#00AD83; border-radius:5px;">Login</button>
</form>
</div>
<div class="card-footer text-muted" style="text-align:center">
New user? <span><a href="registration.html">Register Here</a></span>
</div>
</div>
</div>
</div>
</body>
</html>
