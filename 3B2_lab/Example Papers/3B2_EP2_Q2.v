module counter(
    input clk,
    input rst,
    output reg [6:0]bcd
);
    reg [25:0] big_count = 26'd0;
    reg [3:0] digit_count = 4'd0;
    wire enable;
    always@(posedge clk) begin
        big_count <= big_count + 1'b1;
    end
    assign enable = (big_count == 26'd0);

    always@(posedge clk) begin
        if (enable) begin
            if (digit_count == 4'd9) 
                digit_count <= 4'd0;
            else
                digit_count <= digit_count + 1'b1;
        end
    end

endmodule;