;; Emacs Lisp
;; Run this file:
;; emacs --script scope_dynamic.el

;; --------------------------------------------------



(defvar x 10)  ;; Global variable

(defun outer ()
  (setq y 20)  ;; Dynamic variable (local to outer)
  (inner))

(defun inner ()
  (setq z 30)  ;; Dynamic variable (local to inner)
  (message "x: %d, y: %d, z: %d" x y z))

(outer)
;; Output: "x: 10, y: 20, z: 30"


