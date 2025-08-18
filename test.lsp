(defun read-csv-lines (filename / file lines line)
  (setq lines '())
  (if (setq file (open filename "r"))
    (progn
      (while (setq line (read-line file))
        (setq lines (append lines (list line)))
      )
      (close file)
    )
  )
  lines
)

(defun c:UpdateMLeadersFromCSV ( / csv path ss i ent obj col att tag val lines count)
  (setq tag "KEY_NO") ; Attribute tag to update

  ;; Prompt user for CSV file path
  (setq path (getfiled "Select CSV file" "" "csv" 0))

  (if (not path)
    (progn
      (princ "\nNo file selected.")
      (princ)
    )
    (progn
      ;; Read lines from CSV
      (setq lines (read-csv-lines path))
      (setq count (length lines))

      (if (= count 0)
        (princ "\nCSV file is empty or unreadable.")
        (progn
          ;; Get all multileaders
          (setq ss (ssget "X" '((0 . "MULTILEADER"))))
          (if ss
            (progn
              (setq i 0)
              (while (and (< i (sslength ss)) (< i count))
                (setq ent (ssname ss i))
                (setq obj (vlax-ename->vla-object ent))
                (setq val (nth i lines)) ; Get corresponding value from CSV

                ;; Only update if it's block-based MLeader
                (if (= (vla-get-contenttype obj) 2) ; acBlockContent
                  (progn
                    (setq col (vla-get-blockcontent obj))
                    (vlax-for att col
                      (if (and
                            (= (vla-get-objectname att) "AcDbAttribute")
                            (= (strcase (vla-get-tagstring att)) (strcase tag))
                          )
                        (vla-put-textstring att val)
                      )
                    )
                  )
                )
                (setq i (1+ i))
              )
              (princ (strcat "\nUpdated " (itoa i) " MLeader(s) with values from CSV."))
            )
            (princ "\nNo multileaders found in drawing.")
          )
        )
      )
    )
  )
  (princ)
)
