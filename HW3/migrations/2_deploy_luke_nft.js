const lukeNFT = artifacts.require('lukeNFT');
module.exports = function (deployer) {
deployer.deploy(lukeNFT);
};