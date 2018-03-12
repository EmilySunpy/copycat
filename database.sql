CREATE TABLE `connections` (
  `UUID_FROM` int(11) NOT NULL,
  `UUID_TO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `nodes` (
  `UUID` int(11) NOT NULL,
  `type` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `value` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


ALTER TABLE `nodes`
  ADD UNIQUE KEY `UUID` (`UUID`);