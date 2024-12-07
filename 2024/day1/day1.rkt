#lang racket

(define (read-file filename)
  (call-with-input-file filename
    (lambda (port)
      (letrec ((read-lines
                 (lambda (lines)
                   (let ((line (read-line port)))
                     (cond [(eof-object? line) lines]
                           [else (read-lines (append lines (list line)))])))))
        (read-lines '())))))


(define (transpose data)
  (let ([num-cols (length (car data))])
    (for/list ([col (range num-cols)])
      (for/list ([row data])
        (list-ref row col))))
)

(define (convert-to-int-cols data)
  (transpose (map (lambda (line) (map string->number (string-split line))) data)))

(define input-file "sample.txt")

(define (sort-lists lists)
  (for/list ([lst lists])
    (sort lst <))
)


(define (diff lists)
  (display lists)
  (map abs (map - (first lists) (second lists)))
)

(define (abs val)
  (if (< val 0) (* -1 val) val)
)

(define (sum list)
  (foldl (lambda (a b) (+ a b)) 0 list)
)

(sum (diff (sort-lists (convert-to-int-cols (read-file input-file)))))