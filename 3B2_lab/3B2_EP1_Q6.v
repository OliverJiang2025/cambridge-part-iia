module grey_code_counter (
    input clk,
    input rst,
    output reg [2:0] Q
);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            Q <= 3'b000;
        end
        else begin
            if (Q == 3'b000)
                Q <= 3'b001;
            else if (Q == 3'b001)
                Q <= 3'b011;
        end
    end

endmodule;