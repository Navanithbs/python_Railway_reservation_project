#############################################################################
# Generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#  May 26, 2020 08:39:17 PM IST  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 611x402+358+208
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1351 738
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Cancellation Page"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    label $top.lab44 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {Noto Serif Display} -size 21 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Booking Cancellation} 
    vTcl:DefineAlias "$top.lab44" "Label1" vTcl:WidgetProc "Toplevel1" 1
    labelframe $top.lab45 \
        -borderwidth 6 \
        -font {-family {DejaVu Sans} -size 11 -weight bold -slant italic -underline 1} \
        -foreground black -text {Customer Details :} \
        -background $vTcl(actual_gui_bg) -height 125 -highlightcolor black \
        -width 370 
    vTcl:DefineAlias "$top.lab45" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab45
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 11 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text {Name :} 
    vTcl:DefineAlias "$site_3_0.lab46" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 11 -weight bold -slant italic} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Ticket no :} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label3" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent53 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent53" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent54 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent54" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab46 \
        -in $site_3_0 -x 10 -y 30 -width 142 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 10 -y 60 -width 142 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent53 \
        -in $site_3_0 -x 170 -y 30 -width 186 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent54 \
        -in $site_3_0 -x 170 -y 60 -width 186 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but60 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 6 \
        -font {-family {DejaVu Sans} -size 10 -weight bold} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Confirm 
    vTcl:DefineAlias "$top.but60" "Button1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab44 \
        -in $top -x 80 -y 40 -width 419 -relwidth 0 -height 71 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 120 -y 130 -width 370 -relwidth 0 -height 125 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 240 -y 290 -width 141 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

