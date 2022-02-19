.data

.text
    #le x
	addi	$v0, $zero, 5
	syscall

	#le y
	add	$s0, $zero, $v0
	addi	$v0, $zero, 5
	syscall

	#le w
	add	$s1, $zero, $v0
	addi	$v0, $zero, 5
	syscall

	#le z
	add	$s2, $zero, $v0
	addi	$v0, $zero, 5
	syscall

	add	$s3, $zero, $v0

	# soma x + Y
	add	$s7, $s0, $s1
	# soma (x + y) + z
	add	$s7, $s7, $s3

	# x * x
	mul	$s4, $s0, $s0

	# y * y
	mul	$s5, $s1, $s1

	# (y * y) * y
	mul	$s5, $s5, $s1

	#  z * z
	mul	$s6, $s3, $s3
	#  (z * z) * z
	mul	$s6, $s6, $s3
	#  ((z * z) * z) * z
	mul	$s6, $s6, $s3
	
	add	$s7, $s7, $s4
	add	$s7, $s7, $s5
	add	$s7, $s7, $s6
	
	div	$s7, $s2
	
	mflo	$s0 
		
	#Imprime
	addi 	$v0, $zero, 1
	add 	$a0, $zero, $s0
	syscall
	
	#return 0
	addi 	$v0, $zero, 10
	syscall	
