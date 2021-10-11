-- SQLite

/*
%Y = ano
%m = mês
%d = dia

%H = horas
%M = minutos
%S = segundos
*/

-- STRFTIME = STR (string) | F (format) | TIME (tempo)

SELECT DATETIME('NOW', 'localtime') AS 'Data atual do seu Sistema',
       STRFTIME('%Y', DATE('NOW', 'localtime')) - STRFTIME('%Y', DATE('1991-03-05')) AS 'Anos'
