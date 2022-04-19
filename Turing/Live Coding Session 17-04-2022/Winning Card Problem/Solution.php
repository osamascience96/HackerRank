<?php
    class Solution{
        
        private $CardsDeck;

        function __construct($CardsDeck)
        {
            $this->CardsDeck = $CardsDeck;
        }

        function Solve(){
            print_r($this->CardsDeck);
        }
    }

    $inputs = json_decode(file_get_contents("input.json"), true);
    foreach($inputs as $input){
        $solution = new Solution($input);
        $solution->Solve();
    }
?>