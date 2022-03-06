pragma solidity ^0.8.11;

contract Calculator {

    function add(int256 x, int256 y) public pure returns (int256 result) {
        return x+y;
    }

    function sub(int256 x, int256 y) public pure returns (int256 result) {
        return x-y;
    }

    function mul(int256 x, int256 y) public pure returns (int256 result) {
        return x*y;
    }

    function div(int256 x, int256 y) public pure returns (int256 result) {
        return x/y;
    }

}