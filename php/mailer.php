<?php

class Mailer {
	private $from_email;
	private $from_name;
	
	protected $get_message = 'SELECT content, subject FROM Emails WHERE type=:type;';
	protected $get_user = 'SELECT first_name, last_name, email FROM Users WHERE id=:id;';
	
	const CRLF = "\r\n";
	
	public function __construct($from_email, $from_name, $db) {
		this->$from_email = $from_email;
		this->$from_name = $from_name;
		this->$db = $db;
	}
	
	public function send($to, $message_type) {
		$locations = json_decode($to, true);
		
		$stmt = this->$db->prepare(this->$get_message);
		$stmt->execute(
			array(
				'type' => $message_type
			)
		);
		
		
	}
}