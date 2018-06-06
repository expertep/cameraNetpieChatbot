<?php 

 require("pub.php");
$method = $_SERVER['REQUEST_METHOD'];

// Process only when method is POST
if($method == 'POST'){
		$requestBody = file_get_contents('php://input');
		$json = json_decode($requestBody);
		$intent = $json->result->parameters->intent;


		$response = new \stdClass();

		switch ($intent) {
			case 'LED':
				$sw = $json->result->parameters->sw;
				$led = $json->result->parameters->led;
				$sw = $sw.$led;
				$Topic = "smarthome" ;
				getMqttfromlineMsg($Topic,$sw);
				break;
			case 'CAMERA':
				$cap = 'yes';
				$Topic = "CAMERA" ;
				getMqttfromlineMsg($Topic,$cap);
				break;
			case 'DIM':
				$led = $json->result->parameters->led;
				$value = $json->result->parameters->value;
				if ($value > 255) {
					$value=255;
				}
				else if($value < 0) {
					$value=0;
				}
				$cap="3".$led.$value;
				$speech=$cap;
				//$response->speech = $speech;
				//$response->displayText = $speech;
				$Topic = "smarthome" ;
				getMqttfromlineMsg($Topic,$cap);
				break;
			default:
				$speech = "Sorry, I didnt get that. Please ask me something else.";
				break;
		}
		
		//$response->speech = $speech;
		//$response->displayText = $speech;
		$response->source = "webhook";
		echo json_encode($response);

}
else
{
	echo "Method not allowed";
}

?>