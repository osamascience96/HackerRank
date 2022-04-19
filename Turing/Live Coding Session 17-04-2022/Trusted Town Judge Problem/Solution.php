<?php
    class Solution{
        private $N;
        private $trust;

        function __construct($N, $trust)
        {
            $this->N = $N;
            $this->trust = $trust;
        }

        function Solve(){
            print_r($this->N . "\n");
            print_r($this->trust);
        }
    }


    $inputs = json_decode(file_get_contents("input.json"), true);
    foreach($inputs as $input){
        $solution = new Solution($input["N"], $input["trust"]);
        $solution->Solve();
    }
?>