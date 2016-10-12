<?php
$get_filename = "./user_check.txt";
$put_filename = "./user_info.txt";
copy($get_filename,$put_filename);
unlink($get_filename);
?>
<!DOCTYPE html>
<html>
  <head>
    <title>登録完了</title>
    <meta charset="utf-8">
    <script>
    </script>
  </head>
  <body>
　　　　<h1>確認画面</h1>
    <p>登録が完了しました。ウィンドウを閉じてください。</p>



<footer>
Copyright &copy 山形大学工学部情報科学科井上研究室 All Rights Reserved.
</footer>
  </body>
</html>

