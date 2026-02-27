module tlc(
	input wire clk,
	input wire req,
	input wire rst,
	output reg [4:0] dout
	);
	
	localparam G = 2'd0;
	localparam Y = 2'd1;
	localparam R = 2'd2;
	
	reg [1:0] state;
	reg [28:0] count;
	reg req_latch;
	
	always@(posedge clk or negedge rst) begin
		if (!rst) begin
			state <= G;
			count <= 29'd0;
		end else begin
			case (state)
				G: begin
					if (req == 1'b0) begin
						req_latch <= 1'b1;
					end
					if (count < 29'd500000000 ) begin
						count <= count + 29'd1;
					end 
					if ((count >= 29'd500000000) && ((req == 1'b0)||(req_latch == 1'b1))) begin
						state <= Y;
						count <= 29'd0;
						req_latch <= 1'b0;
					end
				end
				Y: begin
					if (count == 29'd250000000) begin
						state <= R;
						count <= 29'd0;
					end else begin
						count <= count + 29'd1;
					end
				end
				R: begin 
					if (count == 29'd500000000) begin
						state <= G;
						count <= 29'd0;
					end else begin 
						count <= count + 29'd1;
					end
				end
				default: begin
					state <= G;
					count <= 29'd0;
				end
			endcase
		end
	end
	
	always@(*)begin
		case (state)
			G: dout = 5'b10001;
			Y: dout = 5'b01001;
			R: dout = 5'b00110;
			default: dout = 5'b10001;
		endcase
	end
endmodule
			
	