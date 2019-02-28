library(DiagrammeR)
mermaid("
gantt
        dateFormat  YYYY-DD-MM
        title AVI sampling

        
        section tg/cre
        17-20wk                       :active,        first_2,    2017-06-03, 40w
        5wk                           :               first_3,    2017-09-15, 8w
        12wk                          :               first_4,    2017-15-03, 36w
        
        section wt
        12wk                          :crit, done,    import_1,   2017-15-03,2d
        17-20wk                       :crit, done,    import_2,   after import_1, 16w
        5wk                           :crit, active,  import_3,   2017-06-07, 16w
        ")
