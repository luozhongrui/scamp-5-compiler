scamp5_kernel_begin();
movx(A, C, north);
movx(B, C, south);
add(A, A, B);
add(A, A, C);
add(A, A, C);
movx(B, A, east);
movx(A, A, west);
sub(B, B, A);
abs(D, B);
movx(A, C, east);
movx(B, C, west);
add(A, A, B);
add(A, A, C);
add(A, A, C);
movx(B, A, south);
movx(A, A, north);
sub(B, B, A);
abs(A, B);
add(E, A, D);
scamp5_kernel_end();