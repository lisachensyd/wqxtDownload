import jwt

encoded = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjoyLCJ0IjoxNTgwNzI5MDQwMDAwLCJiIjoiMzIwODQwMSIsInciOjEwMDAsImsiOiJ7XCJ1XCI6XCJFN3duSm9MWEtmZz1cIixcImlcIjpcIk8zbHlTOWVtcDRGRWlqVDdTbFZZZ0E9PVwiLFwidFwiOlwiOTdUOW5IWFVvUDZUUTNFT2c3OU4zQT09XCIsXCJiXCI6XCJPakxrcXNUOFlOWT1cIixcIm5cIjpcInpUZm1nUkhzTExrPVwifSIsImlhdCI6MTU4MDcyOTA0MH0.aR821q4IcZ_7-phy1_CONgjo3FUZoKkDa3hpWqdvil4'
jwt_secret = 'g0NnWdSE8qEjdMD8a1aq12qEYphwErKctvfd3IktWHWiOBpVsgkecur38aBRPn2w'
de = jwt.decode(encoded, jwt_secret, algorithms=['HS256'])
print(de)