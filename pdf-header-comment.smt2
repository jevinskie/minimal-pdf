(set-logic QF_BV)

; Define four 8-bit variables representing the four bytes
(declare-fun b1 () (_ BitVec 8))
(declare-fun b2 () (_ BitVec 8))
(declare-fun b3 () (_ BitVec 8))
(declare-fun b4 () (_ BitVec 8))

; Ensure all bytes have their high bit set (i.e., are >= 0x80)
(assert (bvsge b1 #x80))
(assert (bvsge b2 #x80))
(assert (bvsge b3 #x80))
(assert (bvsge b4 #x80))

; UTF-8 encoding constraints for two 2-byte characters
; First byte of each 2-byte character should be between 0xC2 and 0xDF
(assert (bvule #xC2 b1))
(assert (bvule b1 #xDF))
(assert (bvule #xC2 b3))
(assert (bvule b3 #xDF))

; Second byte of each 2-byte character should be between 0x80 and 0xBF
(assert (bvule #x80 b2))
(assert (bvule b2 #xBF))
(assert (bvule #x80 b4))
(assert (bvule b4 #xBF))

; Check for satisfiability
(check-sat)

; Output all satisfying models
(get-model)
