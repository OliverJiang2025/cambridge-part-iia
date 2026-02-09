module lock ( 
    input clk,
    input rst,
    input wire [1:0] s,
    output reg [1:0] Q
);
    wire Sx, Rx, Sy, Ry;

    assign Sx = s[1] & s[0] & Q[0];
    assign Rx = (~s[1]) & s[0] & Q[0];
    assign Sy = (~Q[1] & ~s[1] & s[0])||(Q[1] & s[1] & s[0]);
    assign Ry = (~s[0] & Q[1]);
    
    always@(posedge clk or posedge rst) begin
        if (rst) begin
            Q[1] <= 0;
            Q[0] <= 0;
        end
        else begin
            if (Rx) 
                Q[1] <= 0;
            else if (Sx)
                Q[1] <= 1;
            if (Ry)
                Q[0] <= 0;
            else if (Sy)
                Q[1] <= 1;
        end

    end

endmodule;