<?php
$get_filename = "./user_check.txt";
$put_filename = "./user_info/user_info.txt";
copy($get_filename,$put_filename);
unlink($get_filename);
?>
<!DOCTYPE html>
<html>
  <head>
    <title>登録完了</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="write.css">
    <script>
    </script>
  </head>
  <body>

　　　　<header>
      <div id ="logo"><img src="./image/logo.png" width ="80px" height="80px" style="float:left;"></div>
      <h1 id="title">登録完了</h1>
    </header>

    <div id="main" style="clear:both;">
    <p>登録が完了しました。ウィンドウを閉じてください。</p>
    </div>

<div id="footer">
Copyright &copy 山形大学工学部情報科学科井上研究室 All Rights Reserved.
</div>
  </body>
</html>

