var _0x5a46 = ['f49bf}', '_again_e', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
            (function(_0x4bd822, _0x2bd6f7) {
                var _0xb4bdb3 = function(_0x1d68f6) {
                    while (--_0x1d68f6) {
                        _0x4bd822['push'](_0x4bd822['shift']());
                    }
                };
                _0xb4bdb3(++_0x2bd6f7);
            }(_0x5a46, 0x1b3));
            var _0x4b5b = function(_0x2d8f05, _0x4b81bb) {                                                                      //Receives a hexadecimal, and returns the associated position
                _0x2d8f05 = _0x2d8f05 - 0x0;                                                                                    //in the array _0x5a46
                var _0x4d74cb = _0x5a46[_0x2d8f05];                                                                             //Gets the position in the array
                return _0x4d74cb;                                                                                               //Returns the position in the array
            };
            function verify() {
                checkpass = document[getElementById]('pass')[value];                                                            //0x0 = getElementById and 0x1 = value
                split = 0x4;                                                                                                    //0x2 = substring
                if (checkpass['substring'](0x0, split * 0x2) == _0x4b5b('0x3')) {                                               //From the position 0 to 7 = picoCTF{
                    if (checkpass['substring'](0x7, 0x9) == '{n') {                                                             //From the position 7 of the password array to the 9 we have {n
                        if (checkpass['substring'](split * 0x2, split * 0x2 * 0x2) == _0x4b5b('0x4')) {                         //From 8 to 16 we have not_this
                            if (checkpass['substring'](0x3, 0x6) == 'oCT') {                                                    //From the position 3 of the password array to the 6 we have oCT
                                if (checkpass['substring'](split * 0x3 * 0x2, split * 0x4 * 0x2) == _0x4b5b('0x5')) {           //From 24 to 31 we have f49bf} this is the last part of the pass so 0x5 = f49bf}
                                    if (checkpass['substring'](0x6, 0xb) == 'F{not') {                                          //From 6 to 11 we have F{not
                                        if (checkpass['substring'](split * 0x2 * 0x2, split * 0x3 * 0x2) == _0x4b5b('0x6')) {   //From 16 to 24 we have _again_e
                                            if (checkpass['substring'](0xc, 0x10) == _0x4b5b('0x7')) {                          //From the position 12 of the password array to the 17 we have 
                                                alert('Password\x20Verified');                                                  //0x8 = 'Password\x20Verified'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                } else {
                    alert('Incorrect\x20password');                                         //0x9 = 'Incorrect\x20password'
                }
            }
            //Final password: picoCTF{*********************}