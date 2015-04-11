rebol [title: "Delai IRM"]

; Machines en fonctions 
; Liste de documents pour senregistrer 

print "waiting..."
port: open/lines tcp://:9098

internet-time: func [][
     local-mean-time: now/time
     zone-designator: now/zone
     greenwich-mean-time: local-mean-time + zone-designator
     biel-mean-time: greenwich-mean-time - 1:00:00
     biel-mean-time-total-seconds: (biel-mean-time/hour * 3600) + (biel-mean-time/minute * 60) + biel-mean-time/second
     beats: biel-mean-time-total-seconds * .01157407407407407407407407407
 ]

set-default-font: func [
"sets default font for /View"
font-blk [block! word!] "block of font attributes"
][
system/standard/face/font: make system/standard/face/font font-blk
system/view/vid/vid-face/font: make system/view/vid/vid-face/font font-blk
foreach [w s] system/view/vid/vid-styles [s/font: make s/font font-blk]
]
    
set-default-font [
     name: "verdana" ;or your favorite font
] 

view/options/offset layout [
	     size system/view/screen-face/size button "Unview" [unview]
        backdrop white
        at 10x10 displayirm: text "IRM : " black font-size 120
        at 340x10 displaytime: text "200"  black font-size 120
        at 550x10 displaymin: text "min" black font-size 120
	;at 850x10 displayitime: text "000" black font-size 120
	at 850x10     b: banner 140x32 rate 1 black
        effect [gradient 0x1 255.255.255 255.255.255]
        feel [engage: func [f a e]
                        [set-face b now/time]]
    	]
    	
    	
forever [
;displayitime/text: internet-time
;show displayitime
    if error? er: try  [
        data: first wait connect: first wait port
        print data
	either data = "0" [ 
			displayirm/text: ""
        		displaytime/text: ""
			displaymin/text: ""
        		show displaytime
			show displayirm
			show displaymin
			]
			[ 
			displayirm/text: "IRM :"
        		displaytime/text: data
			displaymin/text: "min"
        		show displaytime
			show displayirm
			show displaymin
			]
        close connect
        true
    	] 
    	[
        er: disarm :er
        net-error: rejoin [
            		  form now newline
            		  er newline newline 
        		  ]
        print net-error
        close connect
    	]

 
]
