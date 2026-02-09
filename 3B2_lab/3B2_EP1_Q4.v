module seven_seg_decoder(
    input wire [3:0] din,
    output wire [6:0] dout
);
    assign dout = 
        (din == 4'h0) ? 7'b1000000 :
        (din == 4'h1) ? 7'b1111001 :
        (din == 4'h2) ? 7'b0100100 :
        (din == 4'h3) ? 7'b0110000 :
        (din == 4'h4) ? 7'b0011001 :
        (din == 4'h5) ? 7'b0010010 :
        (din == 4'h6) ? 7'b0000010 :
        (din == 4'h7) ? 7'b1111000 :
        (din == 4'h8) ? 7'b0000000 :
        (din == 4'h9) ? 7'b0010000 :
        7'b1111111;
endmodule;

module display (
    input wire [7:0] rom_data,
    output wire [6:0] display1,
    output wire [6:0] display2
);
    seven_seg_decoder decoder_1 (
        .din(rom_data[3:0]),
        .dout(display1)
    );
    seven_seg_decoder decoder_2 (
        .din(rom_data[7:4]),
        .dout(display2)
    );

endmodule;
