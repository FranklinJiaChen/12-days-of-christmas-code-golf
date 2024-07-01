"""
Analyzing CSS colours
"""

# colours={"IndianRed":"#cd5c5c","LightCoral":"#f08080","Salmon":"#fa8072","DarkSalmon":"#e9967a","LightSalmon":"#ffa07a","Red":"#ff0000","Crimson":"#dc143c","FireBrick":"#b22222","DarkRed":"#8b0000","Pink":"#ffc0cb","LightPink":"#ffb6c1","HotPink":"#ff69b4","DeepPink":"#ff1493","MediumVioletRed":"#c71585","PaleVioletRed":"#db7093","Coral":"#ff7f50","Tomato":"#ff6347","OrangeRed":"#ff4500","DarkOrange":"#ff8c00","Orange":"#ffa500","Gold":"#ffd700","Yellow":"#ffff00","LightYellow":"#ffffe0","LemonChiffon":"#fffacd","LightGoldenRodYellow":"#fafad2","PapayaWhip":"#ffefd5","Moccasin":"#ffe4b5","PeachPuff":"#ffdab9","PaleGoldenRod":"#eee8aa","Khaki":"#f0e68c","DarkKhaki":"#bdb76b","Lavender":"#e6e6fa","Thistle":"#d8bfd8","Plum":"#dda0dd","Violet":"#ee82ee","Orchid":"#da70d6","Fuchsia":"#ff00ff","Magenta":"#ff00ff","MediumOrchid":"#ba55d3","MediumPurple":"#9370db","BlueViolet":"#8a2be2","DarkViolet":"#9400d3","DarkOrchid":"#9932cc","DarkMagenta":"#8b008b","Purple":"#800080","Indigo":"#4b0082","DarkSlateBlue":"#483d8b","SlateBlue":"#6a5acd","MediumSlateBlue":"#7b68ee","RebeccaPurple":"#663399","GreenYellow":"#adff2f","Chartreuse":"#7fff00","LawnGreen":"#7cfc00","Lime":"#00ff00","LimeGreen":"#32cd32","PaleGreen":"#98fb98","LightGreen":"#90ee90","SpringGreen":"#00ff7f","MediumSpringGreen":"#00fa9a","MediumSeaGreen":"#3cb371","SeaGreen":"#2e8b57","ForestGreen":"#228b22","Green":"#008000","DarkGreen":"#006400","YellowGreen":"#9acd32","OliveDrab":"#6b8e23","Olive":"#808000","DarkOliveGreen":"#556b2f","MediumAquamarine":"#66cdaa","DarkSeaGreen":"#8fbc8f","LightSeaGreen":"#20b2aa","DarkCyan":"#008b8b","Teal":"#008080","Aqua":"#00ffff","Cyan":"#00ffff","LightCyan":"#e0ffff","PaleTurquoise":"#afeeee","Aquamarine":"#7fffd4","Turquoise":"#40e0d0","MediumTurquoise":"#48d1cc","DarkTurquoise":"#00ced1","CadetBlue":"#5f9ea0","SteelBlue":"#4682b4","LightSteelBlue":"#b0c4de","PowderBlue":"#b0e0e6","LightBlue":"#add8e6","SkyBlue":"#87ceeb","LightSkyBlue":"#87cefa","DeepSkyBlue":"#00bfff","DodgerBlue":"#1e90ff","CornflowerBlue":"#6495ed","RoyalBlue":"#4169e1","Blue":"#0000ff","MediumBlue":"#0000cd","DarkBlue":"#00008b","Navy":"#000080","MidnightBlue":"#191970","Cornsilk":"#fff8dc","BlanchedAlmond":"#ffebcd","Bisque":"#ffe4c4","NavajoWhite":"#ffdead","Wheat":"#f5deb3","Burlywood":"#deb887","Tan":"#d2b48c","RosyBrown":"#bc8f8f","SandyBrown":"#f4a460","GoldenRod":"#daa520","DarkGoldenRod":"#b8860b","Peru":"#cd853f","Chocolate":"#d2691e","SaddleBrown":"#8b4513","Sienna":"#a0522d","Brown":"#a52a2a","Maroon":"#800000","White":"#ffffff","Snow":"#fffafa","Honeydew":"#f0fff0","MintCream":"#f5fffa","Azure":"#f0ffff","AliceBlue":"#f0f8ff","GhostWhite":"#f8f8ff","WhiteSmoke":"#f5f5f5","SeaShell":"#fff5ee","Beige":"#f5f5dc","OldLace":"#fdf5e6","FloralWhite":"#fffaf0","Ivory":"#fffff0","AntiqueWhite":"#faebd7","Linen":"#faf0e6","LavenderBlush":"#fff0f5","MistyRose":"#ffe4e1","Gainsboro":"#dcdcdc","LightGray":"#d3d3d3","LightGrey":"#d3d3d3","Silver":"#c0c0c0","DarkGray":"#a9a9a9","DarkGrey":"#a9a9a9","Gray":"#808080","Grey":"#808080","DimGray":"#696969","DimGrey":"#696969","LightSlateGray":"#778899","LightSlateGrey":"#778899","SlateGray":"#708090","SlateGrey":"#708090","DarkSlateGray":"#2f4f4f","DarkSlateGrey":"#2f4f4f","Black":"#000000"}
## grayless
colours={'IndianRed': '#cd5c5c', 'LightCoral': '#f08080', 'Salmon': '#fa8072', 'DarkSalmon': '#e9967a', 'LightSalmon': '#ffa07a', 'Red': '#ff0000', 'Crimson': '#dc143c', 'FireBrick': '#b22222', 'DarkRed': '#8b0000', 'Pink': '#ffc0cb', 'LightPink': '#ffb6c1', 'HotPink': '#ff69b4', 'DeepPink': '#ff1493', 'MediumVioletRed': '#c71585', 'PaleVioletRed': '#db7093', 'Coral': '#ff7f50', 'Tomato': '#ff6347', 'OrangeRed': '#ff4500', 'DarkOrange': '#ff8c00', 'Orange': '#ffa500', 'Gold': '#ffd700', 'Yellow': '#ffff00', 'LightYellow': '#ffffe0', 'LemonChiffon': '#fffacd', 'LightGoldenRodYellow': '#fafad2', 'PapayaWhip': '#ffefd5', 'Moccasin': '#ffe4b5', 'PeachPuff': '#ffdab9', 'PaleGoldenRod': '#eee8aa', 'Khaki': '#f0e68c', 'DarkKhaki': '#bdb76b', 'Lavender': '#e6e6fa', 'Thistle': '#d8bfd8', 'Plum': '#dda0dd', 'Violet': '#ee82ee', 'Orchid': '#da70d6', 'Fuchsia': '#ff00ff', 'Magenta': '#ff00ff', 'MediumOrchid': '#ba55d3', 'MediumPurple': '#9370db', 'BlueViolet': '#8a2be2', 'DarkViolet': '#9400d3', 'DarkOrchid': '#9932cc', 'DarkMagenta': '#8b008b', 'Purple': '#800080', 'Indigo': '#4b0082', 'DarkSlateBlue': '#483d8b', 'SlateBlue': '#6a5acd', 'MediumSlateBlue': '#7b68ee', 'RebeccaPurple': '#663399', 'GreenYellow': '#adff2f', 'Chartreuse': '#7fff00', 'LawnGreen': '#7cfc00', 'Lime': '#00ff00', 'LimeGreen': '#32cd32', 'PaleGreen': '#98fb98', 'LightGreen': '#90ee90', 'SpringGreen': '#00ff7f', 'MediumSpringGreen': '#00fa9a', 'MediumSeaGreen': '#3cb371', 'SeaGreen': '#2e8b57', 'ForestGreen': '#228b22', 'Green': '#008000', 'DarkGreen': '#006400', 'YellowGreen': '#9acd32', 'OliveDrab': '#6b8e23', 'Olive': '#808000', 'DarkOliveGreen': '#556b2f', 'MediumAquamarine': '#66cdaa', 'DarkSeaGreen': '#8fbc8f', 'LightSeaGreen': '#20b2aa', 'DarkCyan': '#008b8b', 'Teal': '#008080', 'Aqua': '#00ffff', 'Cyan': '#00ffff', 'LightCyan': '#e0ffff', 'PaleTurquoise': '#afeeee', 'Aquamarine': '#7fffd4', 'Turquoise': '#40e0d0', 'MediumTurquoise': '#48d1cc', 'DarkTurquoise': '#00ced1', 'CadetBlue': '#5f9ea0', 'SteelBlue': '#4682b4', 'LightSteelBlue': '#b0c4de', 'PowderBlue': '#b0e0e6', 'LightBlue': '#add8e6', 'SkyBlue': '#87ceeb', 'LightSkyBlue': '#87cefa', 'DeepSkyBlue': '#00bfff', 'DodgerBlue': '#1e90ff', 'CornflowerBlue': '#6495ed', 'RoyalBlue': '#4169e1', 'Blue': '#0000ff', 'MediumBlue': '#0000cd', 'DarkBlue': '#00008b', 'Navy': '#000080', 'MidnightBlue': '#191970', 'Cornsilk': '#fff8dc', 'BlanchedAlmond': '#ffebcd', 'Bisque': '#ffe4c4', 'NavajoWhite': '#ffdead', 'Wheat': '#f5deb3', 'Burlywood': '#deb887', 'Tan': '#d2b48c', 'RosyBrown': '#bc8f8f', 'SandyBrown': '#f4a460', 'GoldenRod': '#daa520', 'DarkGoldenRod': '#b8860b', 'Peru': '#cd853f', 'Chocolate': '#d2691e', 'SaddleBrown': '#8b4513', 'Sienna': '#a0522d', 'Brown': '#a52a2a', 'Maroon': '#800000', 'White': '#ffffff', 'Snow': '#fffafa', 'Honeydew': '#f0fff0', 'MintCream': '#f5fffa', 'Azure': '#f0ffff', 'AliceBlue': '#f0f8ff', 'GhostWhite': '#f8f8ff', 'WhiteSmoke': '#f5f5f5', 'SeaShell': '#fff5ee', 'Beige': '#f5f5dc', 'OldLace': '#fdf5e6', 'FloralWhite': '#fffaf0', 'Ivory': '#fffff0', 'AntiqueWhite': '#faebd7', 'Linen': '#faf0e6', 'LavenderBlush': '#fff0f5', 'MistyRose': '#ffe4e1', 'Gainsboro': '#dcdcdc', 'LightGrey': '#d3d3d3', 'Silver': '#c0c0c0', 'DarkGrey': '#a9a9a9', 'Grey': '#808080', 'DimGrey': '#696969', 'LightSlateGrey': '#778899', 'SlateGrey': '#708090', 'DarkSlateGrey': '#2f4f4f', 'Black': '#000000'}
print("length of dictionary:", len(colours))

# for key, value in colours.items():
#     print(f'"{key}"')


## delete keys with "gray" in them
# for key in list(colours.keys()):
#     if "Gray" in key:
#         del colours[key]

# # check if any values are the same
# values = list(colours.values())
# print(len(values))
# print(len(set(values)))
# # find the keys that are the same value
# for key, value in colours.items():
#     for key2, value2 in colours.items():
#         if key != key2 and value == value2:
#             print(key, key2, value)

# for key in sorted(colours.keys()):
#     print(key)

d = {
"AliceZ":"f0f8g",
"AntiqueWhite":"faebd7",
"Aqua":"hgg",
"Aquamarine":"7gfd4",
"Azure":"f0gg",
"Beige":"f5f5dc",
"Bisque":"ge4c4",
"Black":"hhh",
"BlanchedAlmond":"gebcd",
"Z":"hhg",
"ZViolet":"8a2be2",
"Brown":"a52a2a",
"Burlywood":"deb887",
"CadetZ":"5f9ea0",
"Chartreuse":"7gfh",
"Chocolate":"d2691e",
"Coral":"g7f50",
"CornflowerZ":"6495ed",
"Cornsilk":"gf8dc",
"Crimson":"dc143c",
"Cyan":"hgg",
"xZ":"hh8b",
"xCyan":"h8b8b",
"xGoldenRod":"b8860b",
"xX":"h64h",
"xGrey":"a9"*3,
"xKhaki":"bdb76b",
"xMagenta":"8bh8b",
"xOliveX":"556b2f",
"xOrange":"g8ch",
"xOrchid":"9932cc",
"xRed":"8bhh",
"xSalmon":"e9967a",
"xSeaX":"8fbc8f",
"xSlateZ":"483d8b",
"xSlateGrey":"2f4f4f",
"xTurquoise":"hced1",
"xViolet":"94hd3",
"DeepPink":"g1493",
"DeepSkyZ":"hbgf",
"DimGrey":"69"*3,
"DodgerZ":"1e90g",
"FireBrick":"b22222",
"FloralWhite":"gfaf0",
"ForestX":"228b22",
"Fuchsia":"ghg",
"Gainsboro":"dcdcdc",
"GhostWhite":"f8f8g",
"Gold":"gd7h",
"GoldenRod":"daa520",
"X":"h8h0",
"XYellow":"adg2f",
"Grey":"808080",
"Honeydew":"f0gf0",
"HotPink":"g69b4",
"IndianRed":"cd5c5c",
"Indigo":"4bh82",
"Ivory":"ggf0",
"Khaki":"f0e68c",
"Lavender":"e6e6fa",
"LavenderBlush":"gf0f5",
"LawnX":"7cfch",
"LemonChiffon":"gfacd",
"UZ":"add8e6",
"UCoral":"f08080",
"UCyan":"e0gg",
"UGoldenRodYellow":"fafad2",
"UX":"90ee90",
"UGrey":"d3d3d3",
"UPink":"gb6c1",
"USalmon":"ga07a",
"USeaX":"20b2aa",
"USkyZ":"87cefa",
"USlateGrey":"778899",
"USteelZ":"b0c4de",
"UYellow":"gge0",
"Lime":"hgh",
"LimeX":"32cd32",
"Linen":"faf0e6",
"Magenta":"ghg",
"Maroon":"8hh0",
"QAquamarine":"66cdaa",
"QZ":"hhcd",
"QOrchid":"ba55d3",
"QPurple":"9370db",
"QSeaX":"3cb371",
"QSlateZ":"7b68ee",
"QSpringX":"hfa9a",
"QTurquoise":"48d1cc",
"QVioletRed":"c71585",
"MidnightZ":"191970",
"MintCream":"f5gfa",
"MistyRose":"ge4e1",
"Moccasin":"ge4b5",
"NavajoWhite":"gdead",
"Navy":"hh80",
"OldLace":"fdf5e6",
"Olive":"808h0",
"OliveDrab":"6b8e23",
"Orange":"ga5h",
"OrangeRed":"g45h",
"Orchid":"da70d6",
"PaleGoldenRod":"eee8aa",
"PaleX":"98fb98",
"PaleTurquoise":"afeeee",
"PaleVioletRed":"db7093",
"PapayaWhip":"gefd5",
"PeachPuff":"gdab9",
"Peru":"cd853f",
"Pink":"gc0cb",
"Plum":"dda0dd",
"PowderZ":"b0e0e6",
"Purple":"8h080",
"RebeccaPurple":"663399",
"Red":"ghh",
"RosyBrown":"bc8f8f",
"RoyalZ":"4169e1",
"SaddleBrown":"8b4513",
"Salmon":"fa8072",
"SandyBrown":"f4a460",
"SeaX":"2e8b57",
"SeaShell":"gf5ee",
"Sienna":"a0522d",
"Silver":"c0c0c0",
"SkyZ":"87ceeb",
"SlateZ":"6a5acd",
"SlateGrey":"708090",
"Snow":"gfafa",
"SpringX":"hg7f",
"SteelZ":"4682b4",
"Tan":"d2b48c",
"Teal":"h8080",
"Thistle":"d8bfd8",
"Tomato":"g6347",
"Turquoise":"40e0d0",
"Violet":"ee82ee",
"Wheat":"f5deb3",
"White":"ggg",
"WhiteSmoke":"f5"*3,
"Yellow":"ggh",
"YellowX":"9acd32"
}


#find all colours that values are just a string * 3
for key, value in d.items():
    if value == value[:2]*3:
        print(key, value)

#find all colours that values are just a string * 2
for key, value in d.items():
    if value == value[:3]*2:
        print(key, value)