%macro IO 4
    mov rax,%1
    mov rdi,%2
    mov rsi,%3
    mov rdx,%4
    syscall
%endmacro

section .data
msg1 db 10,"Enter BCD number: "
lenm1 equ $-msg1

msg2 db 10,"Equivalent Hex number: "
lenm2 equ $-msg2

errmsg db 10,"Invalid number!"
lenerr equ $-errmsg

section .bss
num     resb 9
answer  resb 8
factor  resq 1

section .text
global _start

_start:

; INPUT
IO 1,1,msg1,lenm1
IO 0,0,num,9

mov rcx,8
mov rsi,num+7
xor rbx,rbx
mov qword[factor],1

; BCD → Decimal conversion
multiply:
    xor rax,rax
    mov al,[rsi]
    sub al,30h
    cmp al,9
    ja invalid

    mul qword[factor]
    add rbx,rax

    mov rax,10
    mul qword[factor]
    mov qword[factor],rax

    dec rsi
    loop multiply

push rbx

IO 1,1,msg2,lenm2

pop rax
call display

jmp exit

invalid:
IO 1,1,errmsg,lenerr

exit:
mov rax,60
mov rdi,0
syscall

; DISPLAY HEX
display:
    mov rsi,answer+7
    mov rcx,8

letter:
    xor rdx,rdx
    mov rbx,16
    div rbx

    cmp dl,9
    jbe add30
    add dl,7

add30:
    add dl,30h
    mov [rsi],dl

    dec rsi
    dec rcx
    jnz letter

    IO 1,1,answer,8
    ret
    
