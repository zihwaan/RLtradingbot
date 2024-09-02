function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function updateCharts() {
    $.getJSON('/data', function(data) {
        $('#current-price').text(numberWithCommas(data.current_price.toFixed(0)) + ' 원');
        $('#portfolio-value').text(numberWithCommas(data.portfolio_value.toFixed(0)) + ' 원');
        $('#profit-loss').text((data.profit_loss_ratio * 100).toFixed(2) + '%');
        $('#avg-buy-price').text(numberWithCommas(data.avg_buy_price.toFixed(0)) + ' 원');

        // 포트폴리오 구성 계산 및 표시
        var cashRatio = (data.balance / data.portfolio_value) * 100;
        var stockRatio = 100 - cashRatio;
        $('#portfolio-composition').text(`현금: ${cashRatio.toFixed(2)}% / 선물: ${stockRatio.toFixed(2)}%`);

        // 차트 업데이트 로직
        var times = data.trade_history.map(item => new Date(item.timestamp * 1000));
        var prices = data.trade_history.map(item => item.price);

        var priceTrace = {
            x: times,
            y: prices,
            type: 'scatter',
            mode: 'lines',
            name: '가격',
            line: {color: '#333'}
        };

        var buyTrace = {
            x: times.filter((_, i) => data.trade_history[i].action === 'buy'),
            y: prices.filter((_, i) => data.trade_history[i].action === 'buy'),
            type: 'scatter',
            mode: 'markers',
            name: '매수',
            marker: {color: '#666', size: 10, symbol: 'triangle-up'}
        };

        var sellTrace = {
            x: times.filter((_, i) => data.trade_history[i].action === 'sell'),
            y: prices.filter((_, i) => data.trade_history[i].action === 'sell'),
            type: 'scatter',
            mode: 'markers',
            name: '매도',
            marker: {color: '#999', size: 10, symbol: 'triangle-down'}
        };

        var layout = {
            title: '선물 가격 및 거래 내역',
            xaxis: {title: '시간'},
            yaxis: {title: '가격 (원)'}
        };

        Plotly.newPlot('price-chart', [priceTrace, buyTrace, sellTrace], layout);

        // 매매 내역 테이블 업데이트
        var tradeHistoryHtml = '';
        data.trade_history.slice().reverse().forEach(function(trade) {
            tradeHistoryHtml += `
                <tr>
                    <td>${new Date(trade.timestamp * 1000).toLocaleString()}</td>
                    <td>${trade.action}</td>
                    <td>${numberWithCommas(trade.price.toFixed(0))} 원</td>
                    <td>${trade.amount.toFixed(4)}</td>
                    <td>${numberWithCommas(trade.portfolio_value.toFixed(0))} 원</td>
                    <td>${trade.reason || ''}</td>
                </tr>
            `;
        });
        $('#trade-history-table tbody').html(tradeHistoryHtml);
    });
}

// 3초마다 업데이트
setInterval(updateCharts, 3000);

// 초기 업데이트
updateCharts();