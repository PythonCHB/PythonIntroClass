def set_colors(foreground_color = 'blue',
               background_color = 'white',
               link_color       =  'red',
               visited_link_color = 'purple'):

    print "The colors are set to:", ( 'foreground_color',
                                  'background_color',
                                  'link_color',
                                  'visited_link_color')

set_colors(link_color='green')

set_colors(link_color='green', background_color='purple')

set_colors('green', background_color='purple')
